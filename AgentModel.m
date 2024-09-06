
%--- STRANGER SOCIAL INTERACTION MODEL - SSIC MODEL ---%

clc; % clear screen
clear all; % clear all variables & functions
close all; % close figures

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Time settings
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

maxLimY = 1.2;      % graph Y axis max
minLimX = 0;        % graph X axis min
maxLimChangeY = 0.1;
minLimChangeY = -0.1;
numStep =500;
numStepChange =500;
numAgent = 3;
dt=0.1;

k = 1.0; #Psi Cap



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Declare All Variables and Set INITIAL VALUES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Instantaneous
Pa = zeros(numAgent, numStep);
Si = zeros(numAgent, numStep);
Ri = zeros(numAgent, numStep);

%Temporal
Dh = zeros(numAgent, numStep);
Ds = zeros(numAgent, numStep);
Df = zeros(numAgent, numStep);
Li = zeros(numAgent, numStep);
Psi = zeros(numAgent, numStep);

%Difference
dfDh = zeros(numAgent,numStepChange);
dfDs = zeros(numAgent,numStepChange);
dfDf = zeros(numAgent,numStepChange);
dfLi = zeros(numAgent,numStepChange);



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Initialisation of all instantaneous parameters

% Positive Affect Para
beta_Pa = 0.5;

% Personality Para
omega_Ps = 0.5;

% Willingness to Interact Para
beta_Si = 0.5;    % Short-Term

% Readiness to Interact Para
omega_Ri = 0.5;
beta_Ri = 1.0;




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Initialisation of all temporal parameters

% Dynamic Emotions Para
gamma_Dh = 0.1;   % Happiness
lambda_Dh = 0.03;
gamma_Ds = 0.1;   % Sadness
lambda_Ds = 0.03;
gamma_Df = 0.1;   % Fear
lambda_Df = 0.03;

% Willingness to Interact Para
gamma_Li = 0.5;   % Long-Term




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Set all Factors
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% Setting temporal Factors %%%

for i=1:numAgent
  Dh(i, 1) = 0.5;
  Ds(i, 1) = 0.5;
  Df(i, 1) = 0.5;
  Li(i, 1) = 0.5;
end



%%% Setting initial Factors %%%

for t=1:numStep

  %Introvert and Sad Boi
  Ha(1, t) = 0.1; % Happiness
  Sd(1, t) = 0.9; % Sadness
  Fe(1, t) = 0.9; % Fear
  Ex(1, t) = 0.1; % Extrovertness
  Op(1, t) = 0.1; % Openness
  Nu(1, t) = 0.9; % Neuroticism
  Eh(1, t) = 0.9; % Level of Exhaustion

  Nc(1, t) = 0.1; % Cultural Preference Similarities
  Ni(1, t) = 0.1; % Interest Similarities

##  Pa(1, t) = 0.5;    % Positive Affect
##  Si(1, t) = 0.5;    % Short-Term Willingness
##  Ri(1, t) = 0.5;    % Readiness to Interact


  %Ambivert and Neutral
  Ha(2, t) = 0.5; % Happiness
  Sd(2, t) = 0.5; % Sadness
  Fe(2, t) = 0.5; % Fear
  Ex(2, t) = 0.5; % Extrovertness
  Op(2, t) = 0.5; % Openness
  Nu(2, t) = 0.5; % Neuroticism
  Eh(2, t) = 0.5; % Level of Exhaustion

  Nc(2, t) = 0.5; % Cultural Preference Similarities
  Ni(2, t) = 0.5; % Interest Similarities

##  Pa(2) = 0.5;    % Positive Affect
##  Si(2) = 0.5;    % Short-Term Willingness
##  Ri(2) = 0.5;    % Readiness to Interact


  %Extrovert and Happy Af
  Ha(3, t) = 0.9; % Happiness
  Sd(3, t) = 0.1; % Sadness
  Fe(3, t) = 0.1; % Fear
  Ex(3, t) = 0.9; % Extrovertness
  Op(3, t) = 0.9; % Openness
  Nu(3, t) = 0.1; % Neuroticism
  Eh(3, t) = 0.1; % Level of Exhaustion

  Nc(3, t) = 0.9; % Cultural Preference Similarities
  Ni(3, t) = 0.9; % Interest Similarities

##  Pa(3) = 0.5;    % Positive Affect
##  Si(3) = 0.5;    % Short-Term Willingness
##  Ri(3) = 0.5;    % Readiness to Interact

end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Run the model at t=1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for i = 1:numAgent
  % Positive Affect
  Pa(i, 1) = Dh(i, 1) - beta_Pa * Ds(i, 1);

  % Short Term Willingness to Interact
  Si(i, 1) = beta_Si * Pa(i, 1) + (1 - beta_Si) * (omega_Ps * Ex(i, 1) + (1 - omega_Ps) * Op(i, 1)) * Nc(i, 1) * (1 - Eh(i, 1));

  % Experienced Fear
  Psi(i, 1) = 1 / (1 + exp(-k * (Df(i, 1) * Nu(i, 1))));

  % Interaction Readiness
  Ri(i, 1) = beta_Ri * (omega_Ri * Si(i, 1) + (1 - omega_Ri) * Li(i, 1)) * Ni(i, 1) * (1 - Psi(i, 1));
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Run the model at t=2
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for t = 2:numStep
  for i=1:numAgent

    % Positive Affect
    Pa(i, t) = Dh(i, t) - beta_Pa * Ds(i, t);

    % Short Term Willingness to Interact
    Si(i, t) = beta_Si * Pa(i, t) + (1 - beta_Si) * (omega_Ps * Ex(i, t) + (1 - omega_Ps) * Op(i, t)) * Nc(i, t) * (1 - Eh(i, t));

    % Experienced Fear
    Psi(i, t) = 1 / (1 + exp(-k * (Df(i, t) * Nu(i, t))));

    % Interaction Readiness
    Ri(i, t) = beta_Ri * (omega_Ri * Si(i, t) + (1 - omega_Ri) * Li(i, t)) * Ni(i, t) * (1 - Psi(i, t));

  % ---- Temporal Specifications ----

    % Dynamic Emotions
    Dh(i, t) = Dh(i, t-1) + gamma_Dh * (Ha(i,t-1) - lambda_Dh) * Dh(i, t-1) * (1 - Dh(i, t-1)) * dt;
    Ds(i, t) = Ds(i, t-1) + gamma_Ds * (Sd(i,t-1) - lambda_Ds) * Ds(i, t-1) * (1 - Ds(i, t-1)) * dt;
    Df(i, t) = Df(i, t-1) + gamma_Df * (Fe(i,t-1) - lambda_Df) * Df(i, t-1) * (1 - Df(i, t-1)) * dt;

    % Long Term
    Li(i, t) = Li(i,t-1) + gamma_Li * (Si(i,t-1) - Li(i,t-1)) * (1 - Li(i,t-1)) * Li(i,t-1) * dt;
  end

end

% checking equillibria
for t=3:numStepChange
  for i=1:numAgent
    dfDh(i,t) = Dh(i,t-1) - Dh(i, t-2);
    dfDs(i,t) = Ds(i,t-1) - Ds(i, t-2);
    dfDf(i,t) = Df(i,t-1) - Df(i, t-2);
    dfLi(i,t) = Li(i,t-1) - Li(i, t-2);
  end
end



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                  Graphs
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Temporal Variables
  figure('Name', 'Temporal Factors');
  colormap('jet');

  subplot(2,2,1);
  surf(Dh(1:numAgent,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgent]);zlim([minLimX maxLimY]);
  title('Dynamic Happiness')
  hold on

  subplot(2,2,2);
  surf(Ds(1:numAgent,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgent]);zlim([minLimX maxLimY]);
  title('Dynamic Sadness')
  hold on

  subplot(2,2,3);
  surf(Df(1:numAgent,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgent]);zlim([minLimX maxLimY]);
  title('Dynamic Fear')
  hold on

  subplot(2,2,4);
  surf(Li(1:numAgent,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgent]);zlim([minLimX maxLimY]);
  title('Long-Term Willingness to Interact')
  hold on

% Instantaneous Factors
  figure('Name', 'Instantaneous Factors');
  colormap('jet');

  subplot(2,2,1);
  surf(Pa(1:numAgent,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgent]);zlim([minLimX maxLimY]);
  title('Positive Affect')
  hold on

  subplot(2,2,2);
  surf(Si(1:numAgent,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgent]);zlim([minLimX maxLimY]);
  title('Short-Term Willingness to Interact')
  hold on

  subplot(2,2,3);
  surf(Ri(1:numAgent,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgent]);zlim([minLimX maxLimY]);
  title('Readiness to Interact')
  hold on

  subplot(2,2,4);
  surf(Psi(1:numAgent,1:numStep));
  xlabel('time steps');ylabel('agents');zlabel('levels');
  xlim([0 numStep]);ylim([1 numAgent]);zlim([minLimX maxLimY]);
  title('Experienced Fear')
  hold on

% graph equillibria
  figure('Name', 'Equillibria State');

  subplot(2,3,1);
  plot (dfLi(1, 1:numStepChange),'--*');
  title ('#1 - Long-Term Willingness to Interact');
  hold on;

  subplot(2,3,2);
  plot (dfLi(2, 1:numStepChange),'--*');
  title ('#2 - Long-Term Willingness to Interact');
  hold on;

  subplot(2,3,3);
  plot (dfLi(3, 1:numStepChange),'--*');
  title ('#3 - Long-Term Willingness to Interact');
  hold on;

  subplot(2,3,4);
  plot (dfLi(1, 1:numStepChange),'--*');
  title ('#1 - Dynamic Happiness');
  hold on;

  subplot(2,3,5);
  plot (dfLi(2, 1:numStepChange),'--*');
  title ('#2 - ynamic Happiness');
  hold on;

  subplot(2,3,6);
  plot (dfLi(3, 1:numStepChange),'--*');
  title ('#3 - ynamic Happiness');
  hold on;

